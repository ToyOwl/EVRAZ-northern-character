import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-alarm-indicator',
  templateUrl: './alarm-indicator.component.html',
  styleUrls: ['./alarm-indicator.component.scss'],
})
export class AlarmIndicatorComponent {
  @Input()
  hasAlarm: boolean = false;

  @Input()
  hasWarning: boolean = true;
}
