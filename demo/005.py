""" This example demonstrates how to save CPU time by reusing the extracted FMU,
 loaded model description, and FMU instance when simulating the same FMU multiple times """

import shutil

from fmi.emulate import FMI_complex_simulation
from fmi.instance import FMI_instance


def run_VanDerPol():
    # download the FMU
    filename = 'D:/workspace/FMIDemo/resources/BouncingBall.fmu'
    # instantiate the FMU
    unzip, md, fmu_instance = FMI_instance(filename)

    # perform the iteration
    # for i in range(10):
    # reset the FMU instance instead of creating a new one
    fmu_instance.reset()

    # calculate the parameters for this run

    result = FMI_complex_simulation(filename=unzip,
                                    model_description=md,
                                    fmu_instance=fmu_instance)
    print(result)

    # free the FMU instance and unload the shared library
    fmu_instance.freeInstance()
    # delete the temporary directory
    shutil.rmtree(unzip, ignore_errors=True)
    # system.exit
    exit(0)


if __name__ == '__main__':
    run_VanDerPol()
