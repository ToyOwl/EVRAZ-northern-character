import { Injectable } from '@angular/core';
import { map, Observable, of, switchMap, tap } from 'rxjs';
import { Aglomachine } from '../models/aglomachine.interface';
import { Exhauster } from '../models/exhauster.interface';
import { Sensor } from '../models/sensor.interface';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ExhausterDataService {
  private serverURL = 'http://127.0.0.1:8000/api/';
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
              { name: 'В, мм/с', value: 50, isAlarm: false, isWarning: false },
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
          aux_items: sensors,
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

  constructor(private http: HttpClient) {
    this.mockAglomachineData = this.generateMockExhausterData(5);
  }

  public getAllAglomchines(): Observable<Aglomachine[]> {
    return this.http.get(this.serverURL + 'get-all-exhausters-cache-test').pipe(
      map((res: unknown) => res as Exhauster[]),
      switchMap((exhausters: Exhauster[]) => {
        const agloMachines: Aglomachine[] = [];

        agloMachines[0] = {
          name: 'Агломашина 1',
          exhausters: [exhausters[0], exhausters[1]],
        };
        agloMachines[1] = {
          name: 'Агломашина 2',
          exhausters: [exhausters[2], exhausters[3]],
        };
        agloMachines[2] = {
          name: 'Агломашина 3',
          exhausters: [exhausters[4], exhausters[5]],
        };
        
        return of(agloMachines);
      }),
      tap((res) => console.log(res))
    );
  }

  public testData() {
    const data = [
      { 'SM_Exgauster\\[2:27]': 10 },
      { 'SM_Exgauster\\[2:2]': 11 },
      { 'SM_Exgauster\\[2:0]': 12 },
    ];
  }
}
