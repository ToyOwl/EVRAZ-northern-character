
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
    aux_items = []

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
