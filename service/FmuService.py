import shutil

from fmpy.fmi2 import FMU2Slave

from fmi.attribute import FMI_model_description
from fmi.instance import FMI_unzip

"""
beforeSimu仿真前初始化工作
"""


def beforeSimu(filename):
    global fmuSlave
    global model_description
    global fmuDir
    global vrs
    vrs = {}
    fmuDir = FMI_unzip(filename)
    model_description = FMI_model_description(filename)
    for variable in model_description.modelVariables:
        vrs[variable.name] = variable.valueReference

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
    return fmuSlave, model_description, fmuDir


"""
simulation 单步仿真执行
这个可以用作
"""


def simulation_oneStep(stop_time):
    time = 0.0
    stop = model_description.defaultExperiment.stopTime
    step = model_description.defaultExperiment.stepSize
    if step is None:
        step = model_description.defaultExperiment.tolerance

    while time < stop_time and time < stop:
        fmuSlave.doStep(currentCommunicationPoint=time,
                        communicationStepSize=step)
        outputs = fmuSlave.getReal(vrs.values())
        time = time + step
    return outputs


"""
仿真结束后资源回收
"""


def afterSimu():
    fmuSlave.terminate()
    fmuSlave.freeInstance()
    shutil.rmtree(fmuDir, ignore_errors=True)


if __name__ == '__main__':
    url = "D:/workspace\\FMIDemo\\resources\\Ball.fmu"
    beforeSimu(url)
    # 仿真数据的具体时刻
    _time = 1.0
    data = simulation_oneStep(_time)
    afterSimu()
    # 数据可以写文件
    print(data)
    # 服务化后删除这一行代码
    exit(0)
