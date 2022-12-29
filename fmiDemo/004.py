import shutil
import numpy as np
from fmpy.fmi2 import FMU2Slave
from fmi.emulate import FMI_polt_result

from fmi.attribute import FMI_model_description, FMI_model_variables
from fmi.instance import FMI_unzip


def simulate_004(show_plot=True):

    fmu_filename = 'D:/workspace/FMIDemo/resources/CoupledClutches.fmu'
    start_time = 0.0
    threshold = 2.0
    stop_time = 2.0
    step_size = 1e-3

    model_description = FMI_model_description(fmu_filename)
    vrs = {}
    for variable in model_description.modelVariables:
        vrs[variable.name] = variable.valueReference

    vr_inputs = vrs['inputs']
    vr_outputs4 = vrs['outputs[4]']

    unzip = FMI_unzip(fmu_filename)
    fmu = FMU2Slave(guid=model_description.guid,
                    unzipDirectory=unzip,
                    modelIdentifier=model_description.coSimulation.modelIdentifier,
                    instanceName='instance1')

    fmu.instantiate()
    fmu.setupExperiment(startTime=start_time)
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()

    time = start_time

    rows = []

    while time < stop_time:

        fmu.setReal([vr_inputs], [0.0 if time < 0.9 else 1.0])
        fmu.doStep(currentCommunicationPoint=time, communicationStepSize=step_size)
        time += step_size
        inputs, outputs4 = fmu.getReal([vr_inputs, vr_outputs4])
        rows.append((time, inputs, outputs4))
        if outputs4 > threshold:
            print("Threshold reached at t = %g s" % time)
            break

    fmu.terminate()
    fmu.freeInstance()
    shutil.rmtree(unzip, ignore_errors=True)
    result = np.array(rows, dtype=np.dtype([('time', np.float64), ('inputs', np.float64), ('outputs[4]', np.float64)]))
    if show_plot:
        FMI_polt_result(result)
    exit(0)


if __name__ == '__main__':
    simulate_004()
