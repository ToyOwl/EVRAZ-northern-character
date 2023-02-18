import { SensorParam } from "./sensor-param.interface";

export interface Sensor {
  name: string;
  hasAlarm: boolean;
  hasWarning: boolean;
  params: SensorParam[];
}
