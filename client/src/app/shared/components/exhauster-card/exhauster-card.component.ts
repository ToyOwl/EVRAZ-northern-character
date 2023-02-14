import { Component, Input } from '@angular/core';
import { Exhauster } from 'src/app/models/exhauster.interface';

@Component({
  selector: 'app-exhauster-card',
  templateUrl: './exhauster-card.component.html',
  styleUrls: ['./exhauster-card.component.scss'],
})
export class ExhausterCardComponent {
  @Input() exhauster!: Exhauster;
}
