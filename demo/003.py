import shutil

from fmpy import *


def run_VanDerPol():
    filename = 'D:/workspace/FMIDemo/resources/CoupledClutches.fmu'

    unzip = extract(filename)

    # read the model description
    md = read_model_description(unzip)

    # instantiate the FMU
    fmu_instance = instantiate_fmu(unzipdir=unzip, model_description=md)

    # reset the FMU instance instead of creating a new one
    fmu_instance.reset()

    result = simulate_fmu(unzip,
                          model_description=md,
                          fmu_instance=fmu_instance)
    plot_result(result)

    # free the FMU instance and unload the shared library
    fmu_instance.freeInstance()

    # delete the temporary directory
    shutil.rmtree(unzip, ignore_errors=True)
    exit(0)


if __name__ == '__main__':
    run_VanDerPol()
