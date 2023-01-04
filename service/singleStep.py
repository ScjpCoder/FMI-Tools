import shutil

from fmpy.fmi2 import FMU2Slave

from fmi.attribute import FMI_model_description
from fmi.instance import FMI_unzip

'''
一个接口初始化资源
'''


def initFmu(filename):
    model_description = FMI_model_description(filename)
    fmuDir = FMI_unzip(filename)
    vrs = {}
    for variable in model_description.modelVariables:
        vrs[variable.name] = variable.valueReference
    experiment = model_description.defaultExperiment
    model = model_description.coSimulation
    if model is None:
        model = model_description.modelExchange
    fmuSlave = FMU2Slave(guid=model_description.guid,
                         unzipDirectory=fmuDir,
                         modelIdentifier=model.modelIdentifier,
                         instanceName='instance1')
    fmuSlave.instantiate()
    fmuSlave.enterInitializationMode()
    fmuSlave.exitInitializationMode()
    print(experiment)
    return fmuSlave, model_description, fmuDir


'''
获取运行参数
'''


def simuParameters(desc):
    stop_time = desc.defaultExperiment.stopTime
    step_size = desc.defaultExperiment.stepSize
    start_time = desc.defaultExperiment.startTime
    vrs = {}
    for variable in desc.modelVariables:
        vrs[variable.name] = variable.valueReference
    if start_time is None:
        time = 0.0
    else:
        time = start_time
    return time, stop_time, step_size, vrs


'''
一个接口进行单步仿真
'''


def simulation(slave, desc, unZipDir):
    time, stop_time, step_size, vrs = simuParameters(desc)

    while time < stop_time:
        text = input('Press any key to continue, or q to quit....')
        if text == 'q' or text == 'Q':
            break
        slave.doStep(currentCommunicationPoint=time, communicationStepSize=step_size)
        time += step_size
        outputs = slave.getReal(vrs.values())
        if time not in outputs:
            print("time not in outputs")
        rows = outputs
        print(rows)
    slave.terminate()
    slave.freeInstance()
    shutil.rmtree(unZipDir, ignore_errors=True)
    exit(0)


if __name__ == '__main__':
    url = "D:\\workspace\\FMIDemo\\resources\\tiaozhijietiao.fmu"
    fmu, description, unzip = initFmu(url)
    simulation(fmu, description, unzip)
