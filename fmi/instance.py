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


def FMI_instance(unzipdir, model_description):
    return instantiate_fmu(unzipdir, model_description, fmi_type=None, visible=False, debug_logging=False, logger=None,
                           fmi_call_logger=None, library_path=None, early_return_allowed=False, event_mode_used=False,
                           intermediate_update=None)
