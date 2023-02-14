import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExhausterOverviewComponent } from './exhauster-overview/exhauster-overview.component';
import { ExhausterDetailComponent } from './exhauster-detail/exhauster-detail.component';
import { TrendsComponent } from './trends/trends.component';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  declarations: [
    ExhausterOverviewComponent,
    ExhausterDetailComponent,
    TrendsComponent,
  ],
  imports: [CommonModule, SharedModule],
  exports: [
    ExhausterOverviewComponent,
    ExhausterDetailComponent,
    TrendsComponent,
  ],
})
export class PagesModule {}
