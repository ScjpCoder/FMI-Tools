from fmi.attribute import *
from fmi.emulate import *
if __name__ == '__main__':
    fmu = "resources/Rectifier.fmu"
    info = FMI_version_and_type(fmu)

    platform = FMI_platform(fmu)
    print(platform)

    FMI_attribute(fmu)

    desc = FMI_model_description(fmu)
    print(desc)
    # 初始值
    value = FMI_start_values(fmu)
    print(value)

    result = FMI_simple_simulation(fmu)
    print(result)

    FMI_polt_result(result)

    # 设置初始值
    start_time = 0.0
    stop_time = 0.1
    step_size = 1e-6
    # output_interval = 2e-2
    kwargs = {
        'filename': fmu,
        'start_time': start_time,
        'stop_time': stop_time,
        'fmi_type': info,
        'step_size': step_size,
        # 'output_interval': output_interval,
    }
    # 仿真步骤
    result = FMI_complex_simulation(**kwargs)
    print(result)

    FMI_polt_result(result)

    time = result['outputs']
    print(time)
