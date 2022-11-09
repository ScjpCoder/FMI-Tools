import shutil
from fmi.emulate import FMI_complex_simulation, FMI_csv_result
from fmi.instance import FMI_Cs_instance


def run_VanDerPol():
    filename = 'D:/workspace/FMIDemo/fmiResources/VanDerPol.fmu'
    unzip, md, fmu_instance = FMI_Cs_instance(filename)
    fmu_instance.reset()
    start_values = {'mu': 1 * 0.01}
    result = FMI_complex_simulation(filename=unzip,
                                    start_values=start_values,
                                    model_description=md,
                                    fmu_instance=fmu_instance)
    FMI_csv_result("../target/van.csv", result)
    fmu_instance.freeInstance()
    shutil.rmtree(unzip, ignore_errors=True)
    exit(0)


if __name__ == '__main__':
    run_VanDerPol()
