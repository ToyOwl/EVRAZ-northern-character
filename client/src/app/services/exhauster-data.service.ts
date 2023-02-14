import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Aglomachine } from '../models/aglomachine.interface';
import { Exhauster } from '../models/exhauster.interface';

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
        exhausters.push({
          name: `Эксгаустер ${counter}`,
          rotor: `Ротор № ${counter}-${j}`,
          rotorLastChanged: Date.now(),
          rotorChangeExpected: Date.now(),
          subsystems: [],
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
}
