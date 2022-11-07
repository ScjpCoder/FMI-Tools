from fmpy import fmi_info, supported_platforms, read_model_description, dump
from fmpy.util import get_start_values, can_simulate
from fmpy.examples.custom_input import *


def FMI_version_and_type(fmu):
    fmiVersion, fmiType = fmi_info(fmu)
    print("FMI Version: " + fmiVersion)
    print("FMI Type: " + " ".join(str(i) for i in fmiType))
    return " ".join(str(i) for i in fmiType)


def FMI_platform(fmu):
    plat = supported_platforms(fmu)
    print("FMI support PlatForms: " + " ".join(str(i) for i in plat))
    return plat


def FMI_can_simulation(platforms):
    can = can_simulate(platforms)
    print(can)


def FMI_attribute(path):
    dump(path)


def FMI_start_values(fmu):
    values = get_start_values(fmu)
    print(values)


def FMI_default_experiment(fmu):
    description = read_model_description(fmu)
    print(description.defaultExperiment)


def FMI_model_variables(fmu):
    description = read_model_description(fmu)
    for val in description.modelVariables:
        print(val)


def FMI_model_description(fmu):
    return read_model_description(fmu)


def FMI_core_description(fmu):
    description = read_model_description(fmu)
    print("Guid: "+description.guid)
    print("ModelName: " + description.modelName)
    print("FMI Version: " + description.fmiVersion)
    print("Generate Tool:" + description.generationTool)
    print("Generate Time: " + description.generationDateAndTime)
    print("FMI description :" + description.description)
    print("FMI outputs: " + " ".join(str(i) for i in description.outputs))
    print("UnitDefinitions: " + " ".join(str(i) for i in description.unitDefinitions))


if __name__ == '__main__':
    # fmuPath = "../resources/Rectifier.fmu"
    fmuPath = "D:/workspace/FMIDemo/resources/CoupledClutches.fmu"
    FMI_version_and_type(fmuPath)
    platform = FMI_platform(fmuPath)
    FMI_can_simulation(platform)
    FMI_default_experiment(fmuPath)
    FMI_start_values(fmuPath)
    FMI_core_description(fmuPath)
