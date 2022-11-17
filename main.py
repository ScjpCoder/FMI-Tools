import sys

from fmi.attribute import *
from fmi.emulate import FMI_polt_result, FMI_complex_simulation, FMI_csv_result
import os


def simulation(filename):
    info = FMI_version_and_type(filename)
    print(info)
    platform = FMI_platform(filename)
    print(platform)

    FMI_attribute(filename)

    desc = FMI_model_description(filename)
    print(desc)
    # 初始值
    value = FMI_start_values(filename)
    print(value)

    # 设置初始值
    start_time = 0.0
    stop_time = 1.0
    step_size = 0.001
    kwargs = {
        'filename': filename,
        'start_time': start_time,
        'stop_time': stop_time,
        'fmi_type': info,
        'step_size': step_size,
    }
    # # 仿真步骤
    result = FMI_complex_simulation(**kwargs)
    FMI_csv_result("result.csv", result)
    FMI_polt_result(result)


if __name__ == '__main__':

    current_directory = os.path.dirname(os.path.realpath(sys.argv[0]))
    print(current_directory)
    current = current_directory + "\\resources"
    listdir = os.listdir(current_directory+"\\resources")
    print(listdir)
    for i in listdir:
        print(str(listdir.index(i)+1) +". "+i)
    num = input("请选择要运行的模型:\n")
    index = listdir.__getitem__(int(num) - 1)
    print(index)
    fmu = current+"\\"+index
    simulation(fmu)
