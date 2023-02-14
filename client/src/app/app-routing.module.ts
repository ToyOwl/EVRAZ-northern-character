import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ExhausterOverviewComponent } from './pages/exhauster-overview/exhauster-overview.component';
import { ExhausterDetailComponent } from './pages/exhauster-detail/exhauster-detail.component';
import { TrendsComponent } from './pages/trends/trends.component';

const routes: Routes = [
  { path: 'exhausters', component: ExhausterOverviewComponent },
  { path: 'exhausters/:id', component: ExhausterDetailComponent },
  { path: 'trends', component: TrendsComponent },
  { path: '**', redirectTo: 'exhausters'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
