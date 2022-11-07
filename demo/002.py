
import shutil

from fmpy import *

from fmi.attribute import FMI_model_description
from fmi.instance import FMI_unzip


def run_VanDerPol():

    filename = 'D:/workspace/FMIDemo/resources/VanDerPol.fmu'

    unzip = FMI_unzip(filename)

    # read the model description
    md = FMI_model_description(unzip)

    # instantiate the FMU
    fmu_instance = instantiate_fmu(unzipdir=unzip, model_description=md, fmi_type='ModelExchange')

    # perform the iteration
    for i in range(10):

        # reset the FMU instance instead of creating a new one
        fmu_instance.reset()

        # calculate the parameters for this run
        start_values = {'mu': i * 0.01}

        result = simulate_fmu(unzip,
                              start_values=start_values,
                              model_description=md,
                              fmu_instance=fmu_instance)
        print(result)
    # free the FMU instance and unload the shared library
    fmu_instance.freeInstance()

    # delete the temporary directory
    shutil.rmtree(unzip, ignore_errors=True)


if __name__ == '__main__':
    run_VanDerPol()
