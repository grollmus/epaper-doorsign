import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Message } from '@server/api-interfaces';

@Component({
  selector: 'server-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  hello$ = this.http.get<Message>('/api/hello');
  constructor(private http: HttpClient) {}
}
