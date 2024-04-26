from waflib import TaskGen, Task, Logs
from waflib.ConfigSet import ConfigSet


class MSVCLibGen(Task.Task):
    run_str = 'LIB.EXE /OUT:${TGT} ${SRC}'
    color = 'BLUE'

    def exec_command(self, cmd, **kw):
        """Execute the command"""

        opts = ["/NOLOGO", "/MACHINE:X64"]

        task_gen: TaskGen.task_gen = self.generator
        env: ConfigSet = task_gen.env
        for lp in env.LIBPATH:
            opts.append(f"/LIBPATH:{lp}")
        #for key in env.keys():
        #    value = env[key]
            #Logs.info(f"{key=}, {value=}")
        #lib_path = env.LIBPATH
        #Logs.info(f"{lib_path=}")
        #Logs.info(f"{env.keys()}")
        #Logs.info(f"{task_gen.env=}")
        cmd = cmd[:2] + opts + cmd[2:]
        return super(MSVCLibGen, self).exec_command(cmd, **kw)


def add_lib_task(self, source, target_path: str):
    bibfor_lib_output_file_node = self.bld.bldnode.make_node(target_path)

    new_task = self.create_task("MSVCLibGen")
    new_task.set_inputs(source)
    new_task.set_outputs([bibfor_lib_output_file_node])
    new_task.dep_nodes = source
    return new_task


bibfor_lib_task = None
bibc_lib_task = None


@TaskGen.feature("fcshlib")
@TaskGen.after_method('propagate_uselib_vars')
def make_fc_modifications(self):
    bibfor_gen = self.bld.get_tgen_by_name("asterbibfor")
    bibfor_task_outputs = [task.outputs[0] for task in bibfor_gen.tasks if task.__class__.__name__ == "fc"]

    bibc_gen = self.bld.get_tgen_by_name("asterbibclib")
    bibc_task_outputs = [task.outputs[0] for task in bibc_gen.tasks if task.__class__.__name__ == "c"]

    bibfor_task_outputs.extend(bibc_task_outputs)
    Logs.info(f"{bibfor_task_outputs=}")

    global bibfor_lib_task
    bibfor_lib_task = add_lib_task(self, bibfor_task_outputs, "src/bibfor/bibfor.lib")


@TaskGen.feature("cshlib")
@TaskGen.after_method('propagate_uselib_vars')
@TaskGen.after_method('fcshlib')
def make_c_modifications(self):
    bibc_gen = self.bld.get_tgen_by_name("asterbibclib")
    bibc_task = [task for task in bibc_gen.tasks if task.__class__.__name__ == "cshlib"][0]
    bibc_task_outputs = [task.outputs[0] for task in bibc_gen.tasks if task.__class__.__name__ == "c"]

    global bibfor_lib_task
    if bibfor_lib_task is None:
        Logs.info("bibfor_lib_task is None")
        return
    bibc_task.inputs.extend(bibfor_lib_task.outputs)
    Logs.info(f"{bibc_task.inputs=}")

    global bibc_lib_task
    bibc_lib_task = add_lib_task(self, bibc_task_outputs, "src/bibc/bibclib.lib")


@TaskGen.feature("cxxshlib")
@TaskGen.after_method('propagate_uselib_vars')
@TaskGen.after_method('cshlib')
def make_cxx_modifications(self):
    bibcxx_gen = self.bld.get_tgen_by_name("asterbibcxxlib")
    bibcxx_task = [task for task in bibcxx_gen.tasks if task.__class__.__name__ == "cxxshlib"][0]
    bibcxx_task_outputs = [task.outputs[0] for task in bibcxx_gen.tasks if task.__class__.__name__ == "cxx"]

    Logs.info(f"{bibcxx_task.outputs=}")

    global bibfor_lib_task
    if bibfor_lib_task is None:
        Logs.info("bibfor_lib_task is None")
        return
    global bibc_lib_task
    if bibc_lib_task is None:
        Logs.info("bibc_lib_task is None")
        return
    bibcxx_task.inputs.extend(bibfor_lib_task.outputs)
    bibcxx_task.inputs.extend(bibc_lib_task.outputs)
    Logs.info(f"{bibcxx_task.inputs=}")

    bibfor_lib_task = add_lib_task(self, bibcxx_task_outputs, "src/bibcxx/bibcxxlib.lib")
