export interface Sensor {
  name: string;
  hasAlarm: boolean;
  hasWarning: boolean;
  params: Array<{
    name: string;
    value: number;
    isAlarm: boolean;
    isWarning: boolean;
  }>;
}
