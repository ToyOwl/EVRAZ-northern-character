import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { EMPTY, Observable } from 'rxjs';
import { Exhauster } from 'src/app/models/exhauster.interface';
import { ExhausterDataService } from 'src/app/services/exhauster-data.service';

@Component({
  selector: 'app-exhauster-detail',
  templateUrl: './exhauster-detail.component.html',
  styleUrls: ['./exhauster-detail.component.scss']
})
export class ExhausterDetailComponent {
  $exhauster: Observable<Exhauster> = EMPTY;

  constructor(private exhausterDataService: ExhausterDataService, private route: ActivatedRoute,) {}

  ngOnInit(): void {
    this.$exhauster = this.exhausterDataService.getExhausterById(this.route.snapshot.params['id']);
  }
}
