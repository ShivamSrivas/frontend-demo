import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {TableTemplateDemo} from '../app/table/table.component'

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,TableTemplateDemo],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'demo';
}
