import pathlib

from waflib import TaskGen, Task, Logs
import os


class MSVCLibGen(Task.Task):
    run_str = 'lib /OUT:${TGT} ${SRC}'
    color = 'BLUE'
    def run(self):
        Logs.info(f"{self.inputs=}")

    def exec_command(self, cmd, **kw):
        """Execute the command"""
        environ = None
        if "env" in kw:
            environ = kw["env"]
            del kw["env"]

        if environ is None:
            environ = os.environ.copy()

        output_fp = pathlib.Path(self.outputs[0].abspath())
        output_fp.parent.mkdir(parents=True, exist_ok=True)

        ofiles = output_fp.parent / f"{output_fp.stem}_input_files.txt"
        with open(ofiles, "w") as f:
            for i in self.inputs:
                f.write(f"{i.abspath()}\n")

        environ["MSVC_LIBGEN_LIB_PATH"] = output_fp.as_posix()
        environ["MSVC_LIBGEN_INPUT_FILE_TXT"] = ofiles.as_posix()

        kw["env"] = environ
        kw["shell"] = True

        # Do this for now.
        cmd = f"LIB.exe /NOLOGO /OUT:{output_fp.as_posix()} @{ofiles.as_posix()}".split()
        return super().exec_command(cmd, **kw)


@TaskGen.feature("cprogram")
@TaskGen.after_method('propagate_uselib_vars')
def make_msvc_modifications(self):
    bibfor_gen = self.bld.get_tgen_by_name("asterbibfor")
    bibfor_task_outputs = [task.outputs[0] for task in bibfor_gen.tasks if task.__class__.__name__ == "fc"]

    bibc_gen = self.bld.get_tgen_by_name("asterbibc")
    bibc_task = [task for task in bibc_gen.tasks if task.__class__.__name__ == "cprogram"][0]

    new_task = self.create_task("MSVCLibGen")
    new_task.set_inputs(bibfor_task_outputs)

    bld_path = pathlib.Path(self.bld.bldnode.abspath()).resolve().absolute()
    bibfor_lib_output_file_path = bld_path / "src/bibfor" / "bibfor.lib"

    bibfor_lib_output_file_node = self.bld.bldnode.make_node(
        bibfor_lib_output_file_path.relative_to(bld_path).as_posix())

    new_task.set_outputs([bibfor_lib_output_file_node])
    new_task.dep_nodes = bibfor_task_outputs

    bibc_task.inputs.extend(new_task.outputs)
