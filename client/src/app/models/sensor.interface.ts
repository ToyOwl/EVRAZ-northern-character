export interface Sensor {
  name: string;
  hasCritical: boolean;
  params: {
    name: string;
    value: number;
    isCritical: boolean;
  }[];
}
