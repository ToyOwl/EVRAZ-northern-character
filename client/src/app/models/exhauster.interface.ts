import { Sensor } from './sensor.interface';

export interface Exhauster {
  name: string;
  rotor: string;
  rotorLastChanged: number;
  rotorChangeExpected: number;
  hasCritical: boolean;
  sensors: Sensor[];
}
