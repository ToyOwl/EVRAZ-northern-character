import { Component, OnInit } from '@angular/core';
import { EMPTY, Observable } from 'rxjs';
import { Aglomachine } from 'src/app/models/aglomachine.interface';
import { ExhausterDataService } from 'src/app/services/exhauster-data.service';

@Component({
  selector: 'app-exhauster-overview',
  templateUrl: './exhauster-overview.component.html',
  styleUrls: ['./exhauster-overview.component.scss'],
})
export class ExhausterOverviewComponent implements OnInit {
  $aglomachineData: Observable<Aglomachine[]> = EMPTY;

  constructor(private exhausterDataService: ExhausterDataService) {}

  ngOnInit(): void {
    this.$aglomachineData = this.exhausterDataService.getAllAglomchines();
  }
}
