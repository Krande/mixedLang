import pathlib

from waflib import TaskGen, Task, Logs
import os


class MSVCLibGen(Task.Task):
    run_str = 'LIB.EXE /NOLOGO /OUT:${TGT} ${SRC}'
    color = 'BLUE'

    def exec_command(self, cmd, **kw):
        """Execute the command"""
        environ = None
        if "env" in kw:
            environ = kw["env"]
            del kw["env"]

        if environ is None:
            environ = os.environ.copy()

        kw["env"] = environ
        kw["shell"] = True

        return super(MSVCLibGen, self).exec_command(cmd, **kw)


def add_lib_task(self, source, target_path: str):
    bld_path = pathlib.Path(self.bld.bldnode.abspath()).resolve().absolute()
    bibfor_lib_output_file_node = self.bld.bldnode.make_node(target_path)

    new_task = self.create_task("MSVCLibGen")
    new_task.set_inputs(source)
    new_task.set_outputs([bibfor_lib_output_file_node])
    new_task.dep_nodes = source
    return new_task

@TaskGen.feature("cprogram")
@TaskGen.after_method('propagate_uselib_vars')
def make_msvc_modifications(self):
    bibfor_gen = self.bld.get_tgen_by_name("asterbibfor")
    bibfor_task_outputs = [task.outputs[0] for task in bibfor_gen.tasks if task.__class__.__name__ == "fc"]
    bibfor_shlib_task = [task for task in bibfor_gen.tasks if task.__class__.__name__ == "fcshlib"][0]
    Logs.info(f"{bibfor_shlib_task.outputs=}")

    bibc_gen = self.bld.get_tgen_by_name("asterbibc")
    bibc_task = [task for task in bibc_gen.tasks if task.__class__.__name__ == "cprogram"][0]

    bibfor_lib_task = add_lib_task(self, bibfor_task_outputs, "src/bibfor/bibfor.lib")

    bibc_task.inputs.extend(bibfor_lib_task.outputs)
