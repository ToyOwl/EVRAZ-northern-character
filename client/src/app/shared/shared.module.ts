import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExhausterCardComponent } from './components/exhauster-card/exhauster-card.component';

@NgModule({
  declarations: [ExhausterCardComponent],
  imports: [CommonModule],
  exports: [ExhausterCardComponent],
})
export class SharedModule {}
