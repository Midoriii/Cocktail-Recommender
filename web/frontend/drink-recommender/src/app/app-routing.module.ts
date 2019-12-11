import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EvaluatorComponent } from './pages/evaluator/evaluator.component';
import { HomepageComponent } from './pages/homepage/homepage.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', component: HomepageComponent },
  { path: 'evaluator', component: EvaluatorComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
