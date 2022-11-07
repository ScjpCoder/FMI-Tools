from typing import Union, Sequence, Dict, Any

import numpy as np
from fmpy import simulate_fmu, write_csv, plot_result
from fmpy.fmi1 import _FMU
from fmpy.model_description import ModelDescription


def FMI_simple_simulation(fmu):
    return simulate_fmu(fmu)


def FMI_complex_simulation(filename,

                           start_time: Union[float, str] = None,
                           stop_time: Union[float, str] = None,
                           step_size: Union[float, str] = None,
                           fmi_type: str = None,
                           input: np.ndarray = None,
                           output: Sequence[str] = None,
                           output_interval: Union[float, str] = None,
                           model_description: ModelDescription = None,
                           fmu_instance: _FMU = None,
                           start_values: Dict[str, Any] = {},
                           ):

    return simulate_fmu(filename=filename,
                        start_time=start_time,
                        stop_time=stop_time,
                        step_size=step_size,
                        fmi_type=fmi_type,
                        input=input,
                        output=output,
                        output_interval=output_interval,
                        model_description=model_description,
                        fmu_instance=fmu_instance,
                        start_values=start_values
                        )


def FMI_csv_result(filename, data):
    write_csv(filename=filename, result=data)


def FMI_polt_result(data):
    plot_result(data)


if __name__ == '__main__':
    # fmuPath = "../resources/Rectifier.fmu"
    # fmuPath = "D:/workspace/FMIDemo/resources/CoupledClutches.fmu"
    fmuPath = 'D:/workspace/FMIDemo/resources/Rectifier.fmu'
    result = FMI_simple_simulation(fmu=fmuPath)
    FMI_csv_result(filename="../target/RectifierResult.csv", data=result)
    FMI_polt_result(result)
