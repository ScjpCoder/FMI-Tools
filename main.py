import os
import shutil
import sys

from fmpy.fmi2 import FMU2Slave

from fmi.attribute import *
from fmi.emulate import FMI_polt_result, FMI_complex_simulation, FMI_csv_result
from fmi.instance import FMI_unzip
from utils.FileUtils import write_csv, del_file


def autoExec(filename):
    name = result_name(filename)

    info = FMI_version_and_type(filename)
    print(info)

    platform = FMI_platform(filename)
    print(platform)

    FMI_attribute(filename)

    desc = FMI_model_description(filename)
    print(desc)
    # 初始值
    value = FMI_start_values(filename)
    print(value)

    # 设置初始值
    start_time = 0.0
    stop_time = 1.0
    step_size = 0.001
    kwargs = {
        'filename': filename,
        'start_time': start_time,
        'stop_time': stop_time,
        'fmi_type': info,
        'step_size': step_size,
    }
    # # 仿真步骤
    print("CoSimulation" in info)
    if "CoSimulation" in info:
        kwargs['fmi_type'] = 'CoSimulation'
    result = FMI_complex_simulation(**kwargs)
    FMI_csv_result(name, result)
    FMI_polt_result(result)
    exit(0)


def singleStep(filename):
    name = result_name(filename)
    del_file(name)
    start_time = 0.0
    model_description = FMI_model_description(filename)
    vrs = {}
    for variable in model_description.modelVariables:
        vrs[variable.name] = variable.valueReference

    header = ""
    for i in vrs.keys():
        header = header + i + ","
    header += "\n"

    defaultExperiment = model_description.defaultExperiment
    step_size = defaultExperiment.stepSize
    stop_time = defaultExperiment.stopTime
    unzip = FMI_unzip(filename)
    model = model_description.coSimulation
    if model is None:
        model = model_description.modelExchange
    fmu = FMU2Slave(guid=model_description.guid,
                    unzipDirectory=unzip,
                    modelIdentifier=model.modelIdentifier,
                    instanceName='instance1')

    fmu.instantiate()
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()

    time = start_time
    while time < stop_time:
        text = input('Press any key to continue, or q to quit....')
        if text == 'q' or text == 'Q':
            break
        fmu.doStep(currentCommunicationPoint=time, communicationStepSize=step_size)
        time += step_size
        outputs = fmu.getReal(vrs.values())
        if time not in outputs:
            print("time not in outputs")
        rows = outputs

        write_csv(filename=name, data=rows, header=header)
        print(rows)

    fmu.terminate()
    fmu.freeInstance()
    shutil.rmtree(unzip, ignore_errors=True)
    exit(0)


def result_name(filename):
    items = filename.split("\\")
    model_name = items[len(items) - 1].split(".")[0]
    result_file = model_name + "_result.csv"
    return result_file

if __name__ == '__main__':

    while True:
        current_directory = os.path.dirname(os.path.realpath(sys.argv[0]))
        print(current_directory)
        current = current_directory + "\\resources"
        listdir = os.listdir(current_directory + "\\resources")
        print(listdir)

        for i in listdir:
            print(str(listdir.index(i) + 1) + ". " + i)
        num = input("请选择要运行的模型:\n")
        index = listdir.__getitem__(int(num) - 1)
        print(index)
        fmu = current + "\\" + index

        num = input("请选择要运行的模式:\n1.自动运行\n2.单步运行\n")
        if num == "1":
            autoExec(fmu)
        elif num == "2":
            singleStep(fmu)
        else:
            print("输入无效,请重新选择!")
