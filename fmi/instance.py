from fmpy import extract, instantiate_fmu

from fmi.attribute import FMI_model_description


def FMI_unzip(file):
    return extract(file)


def FMI_Cs_instance(file):
    unzip = extract(file)
    md = FMI_model_description(file)
    instance = instantiate_fmu(unzipdir=unzip,
                               model_description=md,
                               fmi_type='CoSimulation')
    return unzip, md, instance
