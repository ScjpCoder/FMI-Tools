import shutil

from fmpy import *

from fmi.attribute import FMI_model_description
from fmi.emulate import FMI_complex_simulation
from fmi.instance import FMI_unzip, FMI_instance


def run_VanDerPol():
    filename = 'D:/workspace/FMIDemo/resources/VanDerPol.fmu'
    unzip = FMI_unzip(filename)
    md = FMI_model_description(unzip)
    fmu_instance = FMI_instance(unzipdir=unzip, model_description=md)
    fmu_instance.reset()
    # calculate the parameters for this run
    start_values = {'mu': 1 * 0.01}

    result = FMI_complex_simulation(unzip,
                                    start_values=start_values,
                                    model_description=md,
                                    fmu_instance=fmu_instance)
    print(result)
    fmu_instance.freeInstance()
    shutil.rmtree(unzip, ignore_errors=True)


if __name__ == '__main__':
    run_VanDerPol()
