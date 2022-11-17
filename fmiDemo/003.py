import shutil

from fmi.emulate import FMI_complex_simulation, FMI_csv_result
from fmi.instance import FMI_Cs_instance


def simulation_003():
    filename = 'D:/workspace/FMIDemo/resources/BouncingBall.fmu'
    unzip, md, fmu_instance = FMI_Cs_instance(filename)
    fmu_instance.reset()
    result = FMI_complex_simulation(filename=unzip,
                                    model_description=md,
                                    fmu_instance=fmu_instance)
    FMI_csv_result("../target/bb.csv", result)
    fmu_instance.freeInstance()
    shutil.rmtree(unzip, ignore_errors=True)
    exit(0)


if __name__ == '__main__':
    simulation_003()
