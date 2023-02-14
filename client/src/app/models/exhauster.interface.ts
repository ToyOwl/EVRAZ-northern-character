export interface Exhauster {
  name: string;
  rotor: string;
  rotorLastChanged: number;
  rotorChangeExpected: number;
  subsystems: any[];
}
