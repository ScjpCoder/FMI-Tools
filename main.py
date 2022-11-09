from fmi.attribute import *
from fmi.emulate import FMI_polt_result, FMI_complex_simulation

if __name__ == '__main__':
    fmu = "D:/workspace/FMIDemo/resources/Ball.fmu"
    info = FMI_version_and_type(fmu)
    # 设置初始值
    start_time = 0.0
    stop_time = 10.0
    step_size = 1.0
    kwargs = {
        'filename': fmu,
        'start_time': start_time,
        'stop_time': stop_time,
        'fmi_type': info,
        'step_size': step_size,
    }
    # 仿真步骤
    result = FMI_complex_simulation(**kwargs)
    print(result)
    FMI_polt_result(result)
