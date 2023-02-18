import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExhausterCardComponent } from './components/exhauster-card/exhauster-card.component';
import { PrimeModules } from '../prime-modules';
import { AglomachineCardComponent } from './components/aglomachine-card/aglomachine-card.component';
import { DaysSincePipe } from './pipes/days-since.pipe';
import { AppRoutingModule } from '../app-routing.module';
import { AlarmIndicatorComponent } from './components/alarm-indicator/alarm-indicator.component';

@NgModule({
  declarations: [ExhausterCardComponent, AglomachineCardComponent, DaysSincePipe, AlarmIndicatorComponent],
  imports: [CommonModule, AppRoutingModule, ...PrimeModules],
  exports: [ExhausterCardComponent, AglomachineCardComponent],
})
export class SharedModule {}
