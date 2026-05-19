import { Pipe, PipeTransform } from '@angular/core';

/**
 * Quiero que si un string es muy largo, lo acorte y le ponga "..." al final.
 * Ejemplo entrada: "Este ejemplo es muy largo y quiero acortarlo"
 * Ejemplo salida: "Este ejemplo es muy largo..."

  transform(value: unknown, ...args: unknown[])
 */

@Pipe({
  name: 'acortador',//selector del pipe, se usa en el html
})
export class AcortadorPipe implements PipeTransform {
  transform(value: string, largo: number = 12, caracter: string = '...'): string {
    if (value.length > largo) {
      return value.slice(0, largo) + caracter;
    } else {
      return value;
    }
  }
}

/* 
{{variable | pipe}}
{{variable | new Pipe().transform(variable)}}
*/