import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Client } from '@server/api-interfaces';

@Injectable({
  providedIn: 'root'
})
export class ClientService {
  constructor(private readonly httpClient: HttpClient) {}

  getClientList() {
    return this.httpClient.get<Client[]>('/api/client/')
  }
}
