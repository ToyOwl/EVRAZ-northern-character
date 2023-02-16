import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'daysSince' })
export class DaysSincePipe implements PipeTransform {
  transform(date: number): string {
    const date_1 = new Date(date);
    let date_2 = new Date();

    const difference = new Date(date).getTime() - new Date().getTime();
    let totalDays = Math.ceil(difference / (1000 * 3600 * 24));
    return `${totalDays} сут`;
  }
}
