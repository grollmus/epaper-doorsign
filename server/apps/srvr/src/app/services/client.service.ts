import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ClientService {
  constructor(private readonly httpClient: HttpClient) {}

  getClientList() {
    return this.httpClient.get('/api/client/')
  }
}
