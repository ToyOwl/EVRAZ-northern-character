import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExhausterCardComponent } from './components/exhauster-card/exhauster-card.component';
import { PrimeModules } from '../prime-modules';
import { AglomachineCardComponent } from './components/aglomachine-card/aglomachine-card.component';
import { DaysSincePipe } from './pipes/days-since.pipe';

@NgModule({
  declarations: [ExhausterCardComponent, AglomachineCardComponent, DaysSincePipe],
  imports: [CommonModule, ...PrimeModules],
  exports: [ExhausterCardComponent, AglomachineCardComponent],
})
export class SharedModule {}
