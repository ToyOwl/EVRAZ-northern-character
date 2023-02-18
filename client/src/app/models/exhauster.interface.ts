import { SensorParam } from './sensor-param.interface';
import { Sensor } from './sensor.interface';

export interface Exhauster {
  name: string;
  //   rotor: string;
  //   rotorLastChanged: number;
  //   rotorChangeExpected: number;
  hasAlarm: boolean;
  hasWarning: boolean;
  bearings: Sensor[];
  aux_items: SensorParam[];
}
