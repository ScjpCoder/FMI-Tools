from fmpy import simulate_fmu

from fmi.attribute import *
from fmi.emulate import FMI_polt_result, FMI_complex_simulation, FMI_simple_simulation, FMI_csv_result


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

    # result = FMI_simple_simulation(filename)
    # FMI_polt_result(result)
    # print(result)
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
    FMI_csv_result("../target/tiaozhijietiao.csv", result)
    FMI_polt_result(result)
    exit(0)


if __name__ == '__main__':
    fmu = "D:/workspace/FMIDemo/resources/tiaozhijietiao.fmu"
    simulation(fmu)
