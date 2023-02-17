import { Component, Input } from '@angular/core';
import { Aglomachine } from 'src/app/models/aglomachine.interface';

@Component({
  selector: 'app-aglomachine-card',
  templateUrl: './aglomachine-card.component.html',
  styleUrls: ['./aglomachine-card.component.scss'],
})
export class AglomachineCardComponent {
  @Input() aglomachine!: Aglomachine;
}


