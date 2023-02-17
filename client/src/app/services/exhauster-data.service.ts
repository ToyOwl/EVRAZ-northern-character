import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Aglomachine } from '../models/aglomachine.interface';
import { Exhauster } from '../models/exhauster.interface';
import { Sensor } from '../models/sensor.interface';

@Injectable({
  providedIn: 'root',
})
export class ExhausterDataService {
  private mockAglomachineData: Aglomachine[] = [];

  private generateMockExhausterData(n: number): Aglomachine[] {
    const result: Aglomachine[] = [];

    let counter = 0;
    for (let i = 0; i < n; i++) {
      const exhausters: Exhauster[] = [];
      for (let j = 0; j < 2; j++) {
        const sensors: Sensor[] = [];

        for (let k = 0; k < i + j; k++) {
          sensors.push({
            name: `ПС-${k}`,
            hasWarning: false,
            hasAlarm: false,
            params: [
              { name: 'T, °C', value: 100, isAlarm: false, isWarning: false },
              { name: 'В, мм/с', value: 50, isAlarm: false, isWarning: false  },
            ],
          });
        }

        exhausters.push({
          name: `Эксгаустер ${counter}`,
          // rotor: `Ротор № ${counter + i}`,
          hasWarning: false,
          hasAlarm: false,
          // rotorLastChanged: Date.now() - 690061,
          // rotorChangeExpected: Date.now() - 990061,
          bearings: sensors,
          aux_items: sensors
        });
        counter++;
      }
      result.push({
        name: `Агломашина № ${i}`,
        exhausters,
      });
    }

    return result;
  }

  constructor() {
    this.mockAglomachineData = this.generateMockExhausterData(5);
  }

  public getAllAglomchines(): Observable<Aglomachine[]> {
    return of(this.mockAglomachineData);
  }

  public testData(){
    const data = [
      {"SM_Exgauster\\[2:27]": 10},
      {"SM_Exgauster\\[2:2]": 11},
      {"SM_Exgauster\\[2:0]": 12}
    ]
  }
}
