import { faker } from '@faker-js/faker';
import { RoomBooking, RoomInfo } from '../interfaces';

const roomNames = [
  'Cloud',
  'Smalltalk',
  'Unicorn',
  'Waldhüttn',
  'Wiesn',
  'Zugspitze',
];

const randomArray = (length, max) =>
  [...new Array(length)].map(() => Math.round(Math.random() * max));

const booking: RoomBooking = {
  booker: faker.name.fullName(),
  from: faker.date.recent(),
  to: faker.date.future(),
};

export const dummyRoomInfoData: RoomInfo = {
  name: roomNames[Math.floor(Math.random() * roomNames.length) + 1],
  bookings: randomArray(0, 4).map((emptyBooking) => booking),
};
