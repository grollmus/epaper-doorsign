import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Message } from '@server/api-interfaces';
import { Observable } from 'rxjs';
import { ClientService } from './services/client.service';

@Component({
  selector: 'server-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  clientList$: Observable<any>;
  constructor(clientService: ClientService) {
    this.clientList$ = clientService.getClientList();
  }
}
