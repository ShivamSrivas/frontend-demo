
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { Routes, provideRouter } from '@angular/router';

const routes: Routes = []; 

bootstrapApplication(AppComponent, {
  providers: [provideAnimationsAsync(), provideRouter(routes)],
}).catch((err) => console.error(err));
