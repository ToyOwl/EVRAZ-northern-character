
import json

def checkRestrictions(sensors, key):
    for sensor in sensors:
        if sensor[key]:
            return True
    return False

def form_bearings_params(data, mapping):
    params = []
    print("::form bearings params::")
    print(mapping)

    temprature = {}
    temprature['name'] = mapping['temperature_c']##string
    temprature['value'] = data[mapping['temperature']] ## sig from Kafka data
    if(temprature['value'] >= data[mapping['temperature_t']['alarm_max']] or temprature['value'] <= data[mapping['temperature_t']['alarm_min']]):
        temprature['hasAlarm'] = True
    else:
        temprature['hasAlarm'] = False

    if(temprature['value'] >= data[mapping['temperature_t']['warning_max']] or temprature['value'] <= data[mapping['temperature_t']['warning_min']]):
        temprature['hasWarning'] = True
    else:
        temprature['hasWarning'] = False
    params.append(temprature)

    if 'vibration_axial_c' in mapping: 
        vibr_axial = {}
        vibr_axial['name'] = mapping['vibration_axial_c']
        vibr_axial['value'] = data[mapping['vibration_axial']] ## sig from Kafka data
        if(vibr_axial['value'] >= data[mapping['vibration_axial_t']['alarm_max']] or vibr_axial['value'] <= data[mapping['vibration_axial_t']['alarm_min']]):
            vibr_axial['hasAlarm'] = True
        else:
            vibr_axial['hasAlarm'] = False

        if(vibr_axial['value'] >= data[mapping['vibration_axial_t']['warning_max']] or vibr_axial['value'] <= data[mapping['vibration_axial_t']['warning_min']]):
            vibr_axial['hasWarning'] = True
        else:
            vibr_axial['hasWarning'] = False
        params.append(vibr_axial)

    if 'vibration_horizontal_c' in mapping:
        vibr_h = {}
        vibr_h['name'] = mapping['vibration_horizontal_c']##string
        vibr_h['value'] = data[mapping['vibration_horizontal']] ## sig from Kafka data
        if(vibr_h['value'] >= data[mapping['vibration_horizontal_t']['alarm_max']] or vibr_h['value'] <= data[mapping['vibration_horizontal_t']['alarm_min']]):
            vibr_h['hasAlarm'] = True
        else:
            vibr_h['hasAlarm'] = False

        if(vibr_h['value'] >= data[mapping['vibration_horizontal_t']['warning_max']] or vibr_h['value'] <= data[mapping['vibration_horizontal_t']['warning_min']]):
            vibr_h['hasWarning'] = True
        else:
            vibr_h['hasWarning'] = False
        params.append(vibr_h)

    if 'vibration_vertical_c' in mapping:
        vibr_v = {}
        vibr_v['name'] = mapping['vibration_vertical_c']##string
        vibr_v['value'] = data[mapping['vibration_vertical']] ## sig from Kafka data
        if(vibr_v['value'] >= data[mapping['vibration_vertical_t']['alarm_max']] or vibr_v['value'] <= data[mapping['vibration_vertical_t']['alarm_min']]):
            vibr_v['hasAlarm'] = True
        else:
            vibr_v['hasAlarm'] = False

        if(vibr_v['value'] >= data[mapping['vibration_vertical_t']['warning_max']] or vibr_v['value'] <= data[mapping['vibration_vertical_t']['warning_min']]):
            vibr_v['hasWarning'] = True
        else:
            vibr_v['hasWarning'] = False
        params.append(vibr_v)

    return params

def form_sensor(data, mapping, name): ##<-- bearing!!
    print("::form sensors::", name)
    sens = {}
    sens['name'] = name
    sens['params'] = form_bearings_params(data, mapping)
    sens['hasAlarm'] = checkRestrictions(sens['params'], 'hasAlarm')
    sens['hasWarning'] = checkRestrictions(sens['params'], 'hasWarning')
    return sens

def form_aux_items(data, mapping):

    print(mapping)

    aux_items = []

    cool_syst_oil_ta = {}
    cool_syst_oil_ta['name'] = mapping['cooler_system']['oil']['temperature_after_c']
    cool_syst_oil_ta['value'] = data[mapping['cooler_system']['oil']['temperature_after']] ## sig from Kafka data
    cool_syst_oil_ta['hasAlarm'] = False
    cool_syst_oil_ta['hasWarning'] = False
    aux_items.append(cool_syst_oil_ta)

    cool_syst_oil_tb = {}
    cool_syst_oil_tb['name'] = mapping['cooler_system']['oil']['temperature_before_c']
    cool_syst_oil_tb['value'] = data[mapping['cooler_system']['oil']['temperature_before']] ## sig from Kafka data
    cool_syst_oil_tb['hasAlarm'] = False
    cool_syst_oil_tb['hasWarning'] = False
    aux_items.append(cool_syst_oil_tb)

    cool_syst_water_ta = {}
    cool_syst_water_ta['name'] = mapping['cooler_system']['water']['temperature_after_c']
    cool_syst_water_ta['value'] = data[mapping['cooler_system']['water']['temperature_after']] ## sig from Kafka data
    cool_syst_water_ta['hasAlarm'] = False
    cool_syst_water_ta['hasWarning'] = False
    aux_items.append(cool_syst_water_ta)

    cool_syst_water_tb = {}
    cool_syst_water_tb['name'] = mapping['cooler_system']['water']['temperature_before_c']
    cool_syst_water_tb['value'] = data[mapping['cooler_system']['water']['temperature_before']] ## sig from Kafka data
    cool_syst_water_tb['hasAlarm'] = False
    cool_syst_water_tb['hasWarning'] = False
    aux_items.append(cool_syst_water_tb)

    gas_collector_ta = {}
    gas_collector_ta['name'] = mapping['gas_collector']['temperature_after_c']
    gas_collector_ta['value'] = data[mapping['gas_collector']['temperature_after']] ## sig from Kafka data
    gas_collector_ta['hasAlarm'] = False
    gas_collector_ta['hasWarning'] = False
    aux_items.append(gas_collector_ta)

    gas_collector_tb = {}
    gas_collector_tb['name'] = mapping['gas_collector']['temperature_before_c']
    gas_collector_tb['value'] = data[mapping['gas_collector']['temperature_before']] ## sig from Kafka data
    gas_collector_tb['hasAlarm'] = False
    gas_collector_tb['hasWarning'] = False
    aux_items.append(gas_collector_tb)

    gvs_1 = {}
    gvs_1['name'] = mapping['gate_valve_signal']['gas_valve_open_c']
    gvs_1['value'] = data[mapping['gate_valve_signal']['gas_valve_open']] ## sig from Kafka data
    gvs_1['hasAlarm'] = False
    gvs_1['hasWarning'] = False
    aux_items.append(gvs_1)

    gvs_2 = {}
    gvs_2['name'] = mapping['gate_valve_signal']['gas_valve_closed_c']
    gvs_2['value'] = data[mapping['gate_valve_signal']['gas_valve_closed']] ## sig from Kafka data
    gvs_2['hasAlarm'] = False
    gvs_2['hasWarning'] = False
    aux_items.append(gvs_2)

    gvs_3 = {}
    gvs_3['name'] = mapping['gate_valve_signal']['gas_valve_position_c']
    if mapping['gate_valve_signal']['gas_valve_position']:
        gvs_3['value'] = data[mapping['gate_valve_signal']['gas_valve_position']] ## sig from Kafka data
    else: 
        gvs_3['value'] = 0.0
    gvs_3['hasAlarm'] = False
    gvs_3['hasWarning'] = False
    aux_items.append(gvs_3)

    md_1 = {}
    md_1['name'] = mapping['main_drive']['rotor_current_c']
    if mapping['main_drive']['rotor_current']:
        md_1['value'] = data[mapping['main_drive']['rotor_current']] ## sig from Kafka data
    else:
         md_1['value'] = 0.0
    md_1['hasAlarm'] = False
    md_1['hasWarning'] = False
    aux_items.append(md_1)

    md_2 = {}
    md_2['name'] = mapping['main_drive']['rotor_voltage_c']
    if mapping['main_drive']['rotor_voltage']:
        md_2['value'] = data[mapping['main_drive']['rotor_voltage']] ## sig from Kafka data
    else:
        md_2['value'] = 0.0
    md_2['hasAlarm'] = False
    md_2['hasWarning'] = False
    aux_items.append(md_2)

    md_3 = {}
    md_3['name'] = mapping['main_drive']['stator_current_c']
    md_3['value'] = data[mapping['main_drive']['stator_current']] ## sig from Kafka data
    md_3['hasAlarm'] = False
    md_3['hasWarning'] = False
    aux_items.append(md_3)

    md_4 = {}
    md_4['name'] = mapping['main_drive']['stator_voltage_c']
    if mapping['main_drive']['stator_voltage']:
        md_4['value'] = data[mapping['main_drive']['stator_voltage']] ## sig from Kafka data
    else:
        md_4['value'] = 0.0
    md_4['hasAlarm'] = False
    md_4['hasWarning'] = False
    aux_items.append(md_4)

    oil_syst_l = {}
    oil_syst_l['name'] = mapping['oil_system']['oil_level_c']
    oil_syst_l['value'] = data[mapping['oil_system']['oil_level']] ## sig from Kafka data
    oil_syst_l['hasAlarm'] = False
    oil_syst_l['hasWarning'] = False
    aux_items.append(oil_syst_l)

    oil_syst_p = {}
    oil_syst_p['name'] = mapping['oil_system']['oil_pressure_c']
    oil_syst_p['value'] = data[mapping['oil_system']['oil_pressure']] ## sig from Kafka data
    oil_syst_p['hasAlarm'] = False
    oil_syst_p['hasWarning'] = False
    aux_items.append(oil_syst_p)

    main_st = {}
    main_st['name'] = mapping['main_state']['work_c']
    main_st['value'] = data[mapping['main_state']['work']] ## sig from Kafka data
    main_st['hasAlarm'] = False
    main_st['hasWarning'] = False
    aux_items.append(main_st)


    return aux_items

def form_bearings(data, mapping):
    print("::form bearings::")
    ##print(mapping)
    bearings = []
    names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for name in names:
        ##print(mapping[name])
        bearing = form_sensor(data, mapping[name], name)
        bearings.append(bearing)

    return bearings


def form_exgauster(data, mapping, name):
    exg = {}
    
    ##append name
    print("::form exgausters::")
    #print(mapping)
    
    exg['name'] = name

    ##append bearings 
    exg['bearings'] = form_bearings(data, mapping["bearings"])
    exg['aux_items'] = form_aux_items(data, mapping["aux_items"])
    exg['hasAlarm'] = checkRestrictions(exg['bearings'], 'hasAlarm') ##or checkRestrictions(exg['aux_items'], 'hasAlarm')
    exg['hasWarning'] = checkRestrictions(exg['bearings'], 'hasWarning') ##or checkRestrictions(exg['aux_items'], 'hasWarning')

    return exg

def transformData(data):
    with open('exgausters.json', encoding='utf-8') as f:
        mapping = json.load(f)

    exgausters = []

    names = ["1", "2", "3", "4", "5", "6"]
    i = 0
    for exg in mapping: 
        print(i, names[i])

        exgausters.append(form_exgauster(data, exg[names[i]], names[i]))
        i+=1

    return exgausters


if __name__ == '__main__':
    with open('message.json', encoding='utf-8') as f:
        data = json.load(f)

    exgausters = transformData(data)

    print(exgausters)
