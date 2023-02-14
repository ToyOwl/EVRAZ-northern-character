import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExhausterOverviewComponent } from './exhauster-overview/exhauster-overview.component';
import { ExhausterDetailComponent } from './exhauster-detail/exhauster-detail.component';
import { TrendsComponent } from './trends/trends.component';

@NgModule({
  declarations: [
    ExhausterOverviewComponent,
    ExhausterDetailComponent,
    TrendsComponent,
  ],
  imports: [CommonModule],
  exports: [
    ExhausterOverviewComponent,
    ExhausterDetailComponent,
    TrendsComponent,
  ],
})
export class PagesModule {}
