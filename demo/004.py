
import shutil

from fmpy import *


def run_VanDerPol():

    filename = 'D:/workspace/FMIDemo/resources/Rectifier.fmu'

    unzip = extract(filename)

    # read the model description
    md = read_model_description(unzip)

    # instantiate the FMU
    fmu_instance = instantiate_fmu(unzipdir=unzip, model_description= md)

    # perform the iteration
    for i in range(10):

        # reset the FMU instance instead of creating a new one
        fmu_instance.reset()

        # calculate the parameters for this run
        start_values = {'mu': i * 0.01}

        result = simulate_fmu(unzip,
                              model_description=md,
                              fmu_instance=fmu_instance)
        print(result)
    # free the FMU instance and unload the shared library
    fmu_instance.freeInstance()

    # delete the temporary directory
    shutil.rmtree(unzip, ignore_errors=True)
    exit(0)


if __name__ == '__main__':
    run_VanDerPol()
